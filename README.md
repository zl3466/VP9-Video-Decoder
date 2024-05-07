# VP9-Video-Decoder

## Download
`git clone https://github.com/aisu-programming/VP9-Video-Decoder.git`

## Installation
`npm i`

Though I have checked but may have dependency issues.

## Preprocess
Download the zipped data file under [src/encoded_data](https://github.com/aisu-programming/VP9-Video-Decoder/tree/master/src/encoded_data).

Unzip the file and add an underscore (_) before the directory.

Your files should look like this:
> ![image](https://github.com/aisu-programming/VP9-Video-Decoder/assets/66176726/abcabbe9-7e91-431c-b9f1-391166a4470c)
> ![image](https://github.com/aisu-programming/VP9-Video-Decoder/assets/66176726/2d705469-7d9e-4756-9d37-9c9f77b767ea)

## Usage

### Step 1: src/1_format_jsondata.py

The binary img data JSON files are not well formatted:
1. Edit the DATE variable to target date in [src/1_format_jsondata.py](https://github.com/aisu-programming/VP9-Video-Decoder/blob/master/1_format_jsondata.py#L1).
2. Execute it: `python 1_format_jsondata.py`

### Step 2: src/2_extract_groups.py

Extract & format the original logs of scene segments to the decoder's dir
1. Edit the date and root_dir as needed. The root_dir is where the original multiagent and multitraversal logs are stored.
2. Execute it: `python 2_extract_groups.py`

### Step 3: run the backend & the actual webapp App.tsx
The main part of the codes are in [src/App.tsx](https://github.com/aisu-programming/VP9-Video-Decoder/blob/master/src/App.tsx).

To change the target decoding date, simply edit the date at [line 399](https://github.com/aisu-programming/VP9-Video-Decoder/blob/master/src/App.tsx#L399).

To change the function between "Group" and "Traversal", edit the comment at [line 400~403](https://github.com/aisu-programming/VP9-Video-Decoder/blob/master/src/App.tsx#L400:403).
Use 400 & 401 for multiagent decoding, 402 & 403 for multitraversal decoding. They cannot be run simultaneously, have to go one by one.

Run the Back-End App, then run the Front-End App:
1. `python backend.py`
2. `npm start`
3. You should see logs in both the console of the browser and the Back-End App.
