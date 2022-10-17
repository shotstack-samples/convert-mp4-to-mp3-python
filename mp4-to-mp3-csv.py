import shotstack_sdk as shotstack
import os
import sys

from shotstack_sdk.api               import edit_api
from shotstack_sdk.model.clip        import Clip
from shotstack_sdk.model.track       import Track
from shotstack_sdk.model.timeline    import Timeline
from shotstack_sdk.model.output      import Output
from shotstack_sdk.model.edit        import Edit
from shotstack_sdk.model.video_asset import VideoAsset
from shotstack_sdk.model.shotstack_destination import ShotstackDestination


def load_csv(file):
    data = []
    file_handle = open(file, "r")
    lines = file_handle.readlines()
    file_handle.close()
    for line in lines:
        line = line.strip()
        data.append(line)
    return data


if __name__ == "__main__":
    host = "https://api.shotstack.io/stage"
    file_name = "mp4.csv"
    video_links = load_csv(file_name)

    if os.getenv("SHOTSTACK_HOST") is not None:
        host =  os.getenv("SHOTSTACK_HOST")

    configuration = shotstack.Configuration(host = host)

    if os.getenv("SHOTSTACK_KEY") is None:
        sys.exit("API Key is required. Set using: export SHOTSTACK_KEY=your_key_here")  

    configuration.api_key['DeveloperKey'] = os.getenv("SHOTSTACK_KEY") 

    with shotstack.ApiClient(configuration) as api_client:
        for link in video_links:
            api_instance = edit_api.EditApi(api_client)

            video_asset = VideoAsset(
                src=link
            )

            video_clip = Clip(
                asset=video_asset,
                start=0.0,
                length=10.0
            )

            track = Track(clips=[video_clip])

            timeline = Timeline(
                background = "#000000",
                tracks     = [track]
            )
            output = Output(
                format      = "mp3",
                resolution = "preview",
                repeat      = True
            )

            edit = Edit(
                timeline = timeline,
                output   = output
            )

            try:
                api_response = api_instance.post_render(edit)

                message = api_response['response']['message']
                id = api_response['response']['id']

                print(f"{message}\n")
                print(">> Now check the progress of your render by running:")
                print(f">> python examples/status.py {id}")
            except Exception as e:
                print(f"Unable to resolve API call: {e}")