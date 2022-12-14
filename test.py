from asyncio import subprocess
import os
import asyncio
import subprocess
import time

output = "DOWNLOADS"
video_file = "DOWNLOADS/1897713614JXQun/Morning ගනන් 35 සාකච්ඡාව.mp4"

subprocess.run(['ffmpeg','-ss','00:00:01','-i',video_file,'-frames:v','1','-q:v','2','output.jpg']
)
# Take screenshot function
async def take_screen_shot(video_file, output_directory):
    out_put_file_name = output_directory + \
        "/" + str(time.time()) + ".jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        "00:00:01",
        "-i",
        video_file,
        "-vframes",
        "1",
        "-q:v",
        "2",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None