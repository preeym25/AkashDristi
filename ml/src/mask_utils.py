"""
AkashDristi ML - xBD Mask Utilities
File: ml/src/mask_utils.py
Purpose: Convert xBD building polygon annotations into 5-class pixel-level segmentation masks.
"""

import json
import numpy as np
import cv2
import shapely.wkt
from shapely.errors import WKTReadingError

def damage_class_to_id(damage_class):
    """
    Maps an xBD damage subtype string to the corresponding integer class ID.
    
    Classes:
    0 = background
    1 = no-damage (and pre-disaster un-classified buildings)
    2 = minor-damage
    3 = major-damage
    4 = destroyed
    """
    mapping = {
        "no-damage": 1,
        "minor-damage": 2,
        "major-damage": 3,
        "destroyed": 4,
        "un-classified": 1  # Pre-disaster annotations lack damage subtypes, map footprint to 1
    }
    # Return 0 (background) if the damage class string is entirely unrecognized
    return mapping.get(damage_class, 0)

def load_annotations(json_path):
    """
    Reads the xBD JSON annotation file.
    
    Returns:
        dict: The loaded JSON object representing the xBD annotation.
    """
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def create_damage_mask(json_path, image_height, image_width):
    """
    Reads xBD annotations and rasterizes building polygons into a segmentation mask.
    
    Args:
        json_path (str): Path to the xBD JSON annotation file.
        image_height (int): Height of the corresponding image.
        image_width (int): Width of the corresponding image.
        
    Returns:
        np.ndarray: A 2D NumPy array of shape (image_height, image_width) 
                    containing integer class IDs.
    """
    # 1. Initialize empty mask (all 0s for background)
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    
    # 2. Load annotations safely
    try:
        data = load_annotations(json_path)
    except Exception as e:
        print(f"Error loading {json_path}: {e}")
        return mask

    # 3. Extract the 'xy' features array which contains image-coordinate polygons
    features = data.get("features", {}).get("xy", [])
    
    # 4. Iterate over all buildings and process polygons
    for feature in features:
        try:
            # Extract building properties and geometry
            properties = feature.get("properties", {})
            wkt_str = feature.get("wkt")
            
            # Skip if geometry is missing
            if not wkt_str:
                continue
                
            # Extract damage subtype
            # If "subtype" is missing, we default to "no-damage" to ensure the building footprint is captured
            damage_class = properties.get("subtype", "no-damage")
            class_id = damage_class_to_id(damage_class)
            
            # Skip if the class ID maps to background (0)
            if class_id == 0:
                continue

            # Convert WKT polygon geometry into Shapely geometry object
            poly = shapely.wkt.loads(wkt_str)
            
            # Ensure geometry is a Polygon (sometimes MultiPolygons or corrupted shapes can occur)
            if poly.geom_type == 'Polygon':
                # Extract exterior coordinates and format for OpenCV
                coords = np.array(poly.exterior.coords, dtype=np.int32)
                
                # Rasterize polygon into the mask with the correct class ID
                cv2.fillPoly(mask, [coords], class_id)
                
            elif poly.geom_type == 'MultiPolygon':
                # Handle multipolygons by rasterizing each sub-polygon
                for sub_poly in poly.geoms:
                    coords = np.array(sub_poly.exterior.coords, dtype=np.int32)
                    cv2.fillPoly(mask, [coords], class_id)
                    
        except (WKTReadingError, Exception) as e:
            # Handle malformed polygons safely without crashing the dataset processing pipeline
            print(f"Skipping malformed polygon in {json_path}: {e}")
            continue

    return mask