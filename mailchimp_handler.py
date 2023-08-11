import requests

class MailchimpHandler:
    def __init__(self, api_key, server_prefix):
        self.api_key = api_key
        self.base_url = f"https://{server_prefix}.api.mailchimp.com/3.0/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def get_lists(self):
        """Récupère toutes les listes d'audience."""
        response = requests.get(f"{self.base_url}lists", headers=self.headers)
        return response.json()
    
    def add_member_to_list(self, list_id, email_address, status="subscribed", merge_fields=None):
        """Ajoute un membre à une liste spécifique."""
        data = {
            "email_address": email_address,
            "status": status
        }
        if merge_fields:
            data["merge_fields"] = merge_fields
        
        response = requests.post(f"{self.base_url}lists/{list_id}/members", json=data, headers=self.headers)
        return response.json()

    # Vous pouvez ajouter d'autres méthodes pour d'autres endpoints si nécessaire.

# Utilisation:

api_key = "VOTRE_API_KEY"
server_prefix = "VOTRE_SERVER_PREFIX" # Cela peut être 'us20', 'us19', etc., qui fait partie de votre clé API.

handler = MailchimpHandler(api_key, server_prefix)

# Récupérer toutes les listes:
lists_data = handler.get_lists()
print(lists_data)

# Ajouter un membre à une liste spécifique:
response = handler.add_member_to_list("ID_DE_VOTRE_LISTE", "email@example.com")
print(response)
