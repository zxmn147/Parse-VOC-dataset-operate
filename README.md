# Parse-VOC-dataset-operate

Parse VOC dataset annotation file is `xml` format.

You can use annotation tool such as [labelImg](https://github.com/HumanSignal/labelImg) to get the xml.

This tool can quickly adjust the Parse-VOC-dataset, it can help you `replace label` and `remove label`.

Provide statistical data for each label and draw it into a histogram so that you can clearly understand the distribution of the data.

## statistical data

```
python statisticalData.py --xmlPath <your xmlFolder Path>
```

