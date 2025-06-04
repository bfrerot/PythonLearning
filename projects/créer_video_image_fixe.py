#from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
import moviepy

# Charger la vidéo
video = moviepy.VideoFileClip("C:\\PythonLearning\\projects\\vinyl_concept_show_001.wmv")

# Charger l'image et définir sa durée
# image = moviepy.ImageClip("C:\\PythonLearning\\projects\\Image_podcast_1.jpg").with_duration(video.duration)
image = moviepy.ImageClip("C:\\PythonLearning\\projects\\Image_podcast_1.jpg").with_duration(video.duration).resized(width=video.w)
# Créer une vidéo composite (vidéo + image)
final_video = moviepy.CompositeVideoClip([video, image.with_position("center")])

# Exporter la vidéo
final_video.write_videofile("C:\\PythonLearning\\projects\\vinyl_final_001.mp4", codec="libx264")
