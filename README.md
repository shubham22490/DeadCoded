# Reel It by Team Deadcoded

This project is a Python-based video processing application that allows you to download videos from a given URL, generate subtitles for the audio in the video, combine multiple videos into one, and finally generate a video with subtitles and audio.

## Features

1. **Video Downloading**: The application can download videos from a given URL and save them to a specified directory.

2. **Subtitle Generation**: The application can generate subtitles for a given audio file. It uses the AssemblyAI API for this purpose. It also has a function to generate subtitles locally.

3. **Video Combination**: The application can combine multiple videos into one. It also handles videos of different sizes by resizing them to a standard size.

4. **Final Video Generation**: The application can generate a final video with subtitles and audio.


## Highlights

1. **Innovation**: This application brings together several unique features that are not commonly found in other video processing applications. The ability to download videos, generate subtitles, combine videos, and generate a final video makes this application a truly innovative solution.

2. **Advanced Technology**: The application uses several advanced technologies, including the AssemblyAI API for subtitle generation and the moviepy library for video editing. These technologies ensure that the application is at the forefront of video processing.

3. **Ease of Use**: The application is designed to be easy to use, with a simple and intuitive interface. It provides a set of functions that can be easily called from other Python scripts, making it easy to integrate into other projects.

4. **Scalability**: The application is designed to handle a large number of videos and can easily be scaled up to accommodate more users or more extensive video processing tasks.  

5. **Efficiency**: The application makes efficient use of resources, ensuring that videos are processed quickly and without unnecessary use of memory or CPU.  

6. **Reliability** : The application is built with robust error handling and uses reliable libraries and APIs, ensuring that it can handle a variety of inputs and situations without crashing or producing incorrect results.

## Dependencies

The application uses the following Python libraries:

- `os`
- `uuid`
- `requests`
- `srt_equalizer`
- `assemblyai`
- `typing`
- `moviepy.editor`
- `termcolor`
- `datetime`
- `moviepy.video.fx.all`
- `moviepy.video.tools.subtitles`

## How to Use

You can run the program via the main.py file, or you can directly run the .exe file(if it works :( ).

The application provides several functions for video processing:

- `save_video(video_url: str, directory: str = "./temp") -> str`: This function downloads a video from a given URL and saves it to a specified directory. It returns the path to the saved video.

- `generate_subtitles_assemblyai(audio_path: str) -> str`: This function generates subtitles for a given audio file using the AssemblyAI API. It returns the generated subtitles.

- `__generate_subtitles_locally(sentences: List[str], audio_clips: List[AudioFileClip]) -> str`: This function generates subtitles for a given audio file locally. It returns the generated subtitles.

- `generate_subtitles(audio_path: str) -> str`: This function generates subtitles for a given audio file. It first generates the subtitles using the AssemblyAI API, then equalizes the subtitles, and finally saves the subtitles to a file. It returns the path to the generated subtitles.

- `combine_videos(video_paths: List[str], max_duration: int) -> str`: This function combines multiple videos into one. It also handles videos of different sizes by resizing them to a standard size. It returns the path to the combined video.

- `generate_video(combined_video_path: str, tts_path: str, subtitles_path: str) -> str`: This function generates a final video with subtitles and audio. It returns the path to the final video.

## Installation

To use this application, you need to have Python installed on your machine. You can download Python from the official website.

Once you have Python installed, you can clone this repository to your local machine. After cloning the repository, navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

To use the application, you need to import the required functions from the `video.py` file. Here is an example of how to use the application:

```python
from video import save_video, generate_subtitles, combine_videos, generate_video

# Download a video
video_path = save_video("https://example.com/video.mp4")

# Generate subtitles for the video
subtitles_path = generate_subtitles(video_path)

# Combine multiple videos
combined_video_path = combine_videos([video_path, video_path], 60)

# Generate the final video
final_video_path = generate_video(combined_video_path, video_path, subtitles_path)
```

## Contributions

This project was made by [Aditya Singh] , [Shubham Goel] , [Vaishvi Verma],[Nishant Kumar Singh]

## License

This project is licensed under the MIT License.
