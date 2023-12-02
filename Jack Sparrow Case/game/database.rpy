# init python:
#     import sqlite3

#     connect = sqlite3.connect("score_Storage.db")
#     cursor = conn.cursor()

#     class Player:
#         def __init__(self, player_name, overall_score):
#             self.player_name = player_name
#             self.overall_score = overall_score

#             # Save the player to the database
#             cursor.execute("INSERT INTO Player (player_name, overall_score) VALUES (?, ?)",
#                             (self.player_name, self.overall_score))
#             self.id = cursor.lastrowid

#         def update_score(self, new_score):
#                 self.overall_score = new_score

#                 # Update the score in the database
#                 cursor.execute("UPDATE Player SET overall_score = ? WHERE id = ?", (self.overall_score, self.id))

#         def get_overall_score(self):
#             # Query the database for the player's overall score
#             cursor.execute("SELECT overall_score FROM Player WHERE id = ?", (self.id,))
#             result = cursor.fetchone()

#             if result:
#                 return result[0]
#             else:
#                 return None