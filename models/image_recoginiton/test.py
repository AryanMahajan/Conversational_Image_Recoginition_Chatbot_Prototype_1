import xml.etree.ElementTree as ET
import os

def parse_xml_annotations(ann_path, img_name):
    try:
        tree = ET.parse(os.path.join(ann_path, f"{img_name}.xml"))
        root = tree.getroot()
        classes = []

        print("Root:", root)

        for object in root.findall('object'):
            print("Object:", object)
            name = object.find('name').text
            print(name)
            classes.append(name)

        print(classes)
    except Exception as e:
        print(f"Error parsing XML for image {img_name}: {e}")
        return []  # Return an empty list in case of errors

# Example usage:
ann_path = r"models\image_recoginiton\test&train-images\VOC2012_train_val\Annotations"
img_name = "2007_000129"
parse_xml_annotations(ann_path, img_name)
