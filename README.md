# Convert Mp4 To MP3 Using Python & Shotstack API

This Python program converts Mp4 to MP3 using Python, [Shotstack Python SDK](https://pypi.org/project/shotstack-sdk/0.2.1/), and Shotstack API. See [this tutorial](https://shotstack.io/learn/turn-images-to-slideshow-video-using-python/?utm_source=github&utm_campaign=sample_repos) to learn how it works.


### What is Shotstack API?

Shotstack API is a cloud based video editing API that enables you to render multiple videos concurrently. See the available SDKs [here](https://shotstack.io/docs/guide/sdks).  Sign up for a free developer account [here](https://dashboard.shotstack.io/register?utm_source=github&utm_campaign=sample_repos) to get API key. 

### Why use Shotstack API?

Rendering videos is a resource consuming process. It may take several minutes to render one video depending on the
complexity. Shotstack enables to concurrently render multiple videos in the powerful cloud infrastructure. This reduces
rendering time and fastens the process. Visit our [Docs](https://shotstack.io/docs/guide/getting-started/core-concepts/?utm_source=github&utm_campaign=sample_repos) to learn more.

Checkout other Python demo examples in this [Github repo](https://github.com/shotstack/python-demos).


### Installation

Clone this repository with following command

```bash
git clone https://github.com/shotstack-samples/convert-mp4-to-mp3-python.git
```

Go inside the project directory
```bash
cd convert-mp4-to-mp3-python
```

Install the required dependencies including the [Shotstack Python SDK](https://pypi.org/project/shotstack-sdk/0.2.1/)

```bash
pip3 install -r requirements.txt
```


### Set your API key

This program uses the **staging** endpoint by default so use your provided **staging** key:

```bash
export SHOTSTACK_KEY=your_key_here
```

Windows users (Command Prompt):

```bash
set SHOTSTACK_KEY=your_key_here
```

You can [get an API key](http://shotstack.io/register?utm_source=github&utm_campaign=sample_repos) by signing up for a
free developer account.


### Running the program

To run this program, run the `mp4-to-mp3.py` inside the root folder:

```bash
python mp4-to-mp3.py
```

### Final MP3 example

[Here](https://cdn.shotstack.io/au/stage/c9npc4w5c4/aa3bf5f8-822f-4e00-bc43-63f4c93618ac.mp3) is what the final MP3
looks like.

### Accessing rendered media files

To access your rendered files, sign into your Shotstack account. Inside the dashboard, you can find all rendered media
under the Renders tab.

![Alt Text](https://i.postimg.cc/8cCHTZ8V/2022-09-21-11-15-52-Shotstack-Dashboard.png)


### Edit and automate video production using Python

This is just a basic example. You can do way more with Shotstack Python SDK like: 
- Beautify videos by adding effects, transitions, overlays, titles
- Automate media editing and production
- Automatically generat personalized media with code
- Convert media files i.e. gif, mp3, mp4, jpg, bmp, and png
- Generate and add SRT files to multiple videos concurrently
- Use AI to generate media assets to produce videos and more

See our other [tutorial articles](https://shotstack.io/learn/?utm_source=github&utm_campaign=sample_repos) to learn
video editing using Python. 