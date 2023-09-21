class Mediaplayer:
    def play(self, audio_type, filename):
        # interface for media player
        pass

class AdvancedMediaPlayer:
    def play_vlc(self,filename):
        print("playing from VLC")
    def play_mp4(self, filename):
        print("Playing MP4")


class MediaAdapter(Mediaplayer):
    def __init__(self, audio_type, filename):
        self.advanced_player = None
        if audio_type == "vlc":
            self.advanced_player = AdvancedMediaPlayer()
            self.advanced_player.play_vlc(filename)
        if audio_type == "mp4":
            self.advanced_player = AdvancedMediaPlayer()
            self.advanced_player.play_mp4(filename)

    def play(self, audio_type, filename):
        if audio_type == "vlc":
            self.advanced_player.play_vlc(filename)
        if audio_type == "mp4":
            self.advanced_player.play_mp4(filename)

class AudioPlayer(Mediaplayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            return "playing MP3 file "

        adapter = MediaAdapter(audio_type, filename)
        adapter.play(audio_type, filename)

if __name__ == "__main__":
    audio_player = AudioPlayer()
    print(audio_player.play("mp3", "song.mp3"))
    print(audio_player.play("vlc", "movie.vlc"))
    print(audio_player.play("mp4", "video.mp4"))
