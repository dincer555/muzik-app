import requests

class StreamingService:
    def __init__(self, api_key=None):
        self.api_key = api_key
        # Deezer API kullanıyoruz (ücretsiz, API key gerektirmiyor)
        self.base_url = "https://api.deezer.com"
    
    def search_music(self, query):
        """Deezer API ile müzik ara"""
        try:
            response = requests.get(
                f"{self.base_url}/search",
                params={'q': query, 'limit': 20}
            )
            if response.status_code == 200:
                data = response.json()
                results = []
                for track in data.get('data', []):
                    results.append({
                        'id': track['id'],
                        'title': track['title'],
                        'artist': track['artist']['name'],
                        'album': track['album']['title'],
                        'duration': track['duration'],
                        'preview': track['preview'],
                        'cover': track['album']['cover_medium']
                    })
                return results
            return []
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def get_stream_url(self, track_id):
        """Preview URL'si al (30 saniyelik)"""
        try:
            response = requests.get(f"{self.base_url}/track/{track_id}")
            if response.status_code == 200:
                data = response.json()
                return data.get('preview')
            return None
        except Exception as e:
            print(f"Stream error: {e}")
            return None
    
    def get_track_info(self, track_id):
        """Şarkı detaylarını al"""
        try:
            response = requests.get(f"{self.base_url}/track/{track_id}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Track info error: {e}")
            return None
