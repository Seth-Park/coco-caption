import json

def coco_gt_format_save(gt_file):
    gt = json.load(open(gt_file, 'r'))
    gt_dict = {}
    info_dict = {
        'contributor': 'Seth Park',
        'date_created': 'Seth Park',
        'description': 'Seth Park',
        'url': 'Seth Park',
        'version': 'Seth Park',
        'year': 'Seth Park'
    }

    gt_dict['info'] = info_dict
    gt_dict['licenses'] = info_dict
    gt_dict['type'] = 'captions'
    gt_dict['images'] = []
    gt_dict['annotations'] = []

    count = 0
    for k, v in gt.items():
        im = {'filename': k, 'id': k}
        gt_dict['images'].append(im)
        for c in v:
            annotation = {'caption': c, 'id': count, 'image_id': k}
            count += 1
            gt_dict['annotations'].append(annotation)

    json.dump(gt_dict, open(gt_file.split('.json')[0] + '_reformat.json', 'w'))

def coco_gen_format(gen_dict):
    results = []
    for k, v in gen_dict.items():
        results.append({'caption': v, 'image_id': k})
    return results

def coco_gen_format_save(gen_dict, save_path):
    results = coco_gen_format(gen_dict)
    json.dump(results, open(save_path, 'w'))
