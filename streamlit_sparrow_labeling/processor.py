class DataProcessor:

    def __init__(self):
        pass

    def prepare_canvas_data(self, data, background_color, doc_height, doc_width, height, width):
        canvas_rects = []

        for rect in data['words']:
            canvas_rect = self.construct_canvas_rect(rect, doc_height, doc_width, height, width)
            canvas_rects.append(canvas_rect)

        payload = {"version": "4.4.0", "objects": canvas_rects, "background": background_color}

        return payload

    def construct_canvas_rect(self, rect, doc_height, doc_width, height, width):
        canvas_rect = {
            "type": "rect",
            "version": "4.4.0",
            "originX": "left",
            "originY": "top",
            "left": round((rect['rect']['x1'] * width) / doc_width),
            "top": round((rect['rect']['y1'] * height) / doc_height),
            "width": round((rect['rect']['x2'] * width) / doc_width) - round((rect['rect']['x1'] * width) / doc_width),
            "height": round((rect['rect']['y2'] * height) / doc_height) - round((rect['rect']['y1'] * height) / doc_height),
            "fill": "rgba(0, 151, 255, 0.3)",
            "stroke": "rgba(0, 50, 255, 0.7)",
            "strokeWidth": 2,
            "strokeDashArray": None,
            "strokeLineCap": "butt",
            "strokeDashOffset": 0,
            "strokeLineJoin": "miter",
            "strokeUniform": True,
            "strokeMiterLimit": 4,
            "scaleX": 1,
            "scaleY": 1,
            "angle": 0,
            "flipX": False,
            "flipY": False,
            "opacity": 1,
            "shadow": None,
            "visible": True,
            "backgroundColor": "",
            "fillRule": "nonzero",
            "paintFirst": "fill",
            "globalCompositeOperation": "source-over",
            "skewX": 0,
            "skewY": 0,
            "rx": 0,
            "ry": 0
        }

        return canvas_rect

    def prepare_rect_data(self, canvas_data, initial_rects, doc_height, doc_width, height, width):
        rects = []

        for i, canvas_rect in enumerate(canvas_data["objects"]):
            if i < len(initial_rects['words']):
                rect = self.construct_rect(canvas_rect, initial_rects['words'][i], doc_height, doc_width, height, width)
                rects.append(rect)
            else:
                rect = self.construct_rect(canvas_rect, {"value": "", "label": ""}, doc_height, doc_width, height, width)
                rects.append(rect)

        payload = {
            "meta": {
                "version": initial_rects["meta"]["version"],
                "split": initial_rects["meta"]["split"],
                "image_id": initial_rects["meta"]["image_id"],
                "image_size": {
                    "width": initial_rects["meta"]["image_size"]["width"],
                    "height": initial_rects["meta"]["image_size"]["height"]
                }
            },
            "words": rects
        }

        return payload

    def construct_rect(self, canvas_rect, initial_rect, doc_height, doc_width, height, width):
        x2 = canvas_rect['left'] + (canvas_rect['width'] * canvas_rect['scaleX'])
        x2 = round((x2 * doc_width) / width)
        y2 = canvas_rect['top'] + (canvas_rect['height'] * canvas_rect['scaleY'])
        y2 = round((y2 * doc_height) / height)

        rect = {
            "rect": {
                "x1": round((canvas_rect['left'] * doc_width) / width),
                "y1": round((canvas_rect['top'] * doc_height) / height),
                "x2": x2,
                "y2": y2
            },
            "value": initial_rect['value'],
            "label": initial_rect['label']
        }

        return rect

    def update_rect_data(self, rect_data, rect_index, value, label):
        rect_data['words'][rect_index]['value'] = value
        rect_data['words'][rect_index]['label'] = label

        return rect_data