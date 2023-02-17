import osmnx as ox

# dict of algerian wilayas and their codes

algerian_wilayas = {1: "Adrar", 2: "Chlef", 3: "Laghouat", 4: "Oum El Bouaghi",
                    5: "Batna", 6: "Béjaïa", 7: "Biskra", 8: "Béchar", 9: "Blida",
                    10: "Bouira", 11: "Tamanrasset", 12: "Tébessa", 13: "Tlemcen",
                    14: "Tiaret", 15: "Tizi Ouzou", 16: "Alger", 17: "Djelfa",
                    18: "Jijel", 19: "Sétif", 20: "Saïda", 21: "Skikda",
                    22: "Sidi Bel Abbès", 23: "Annaba", 24: "Guelma",
                    25: "Constantine", 26: "Médéa", 27: "Mostaganem", 28: "M'Sila",
                    29: "Mascara", 30: "Ouargla", 31: "Oran", 32: "El Bayadh",
                    33: "Illizi", 34: "Bordj Bou Arreridj", 35: "Boumerdès",
                    36: "El Tarf", 37: "Tindouf", 38: "Tissemsilt", 39: "El Oued",
                    40: "Khenchela", 41: "Souk Ahras", 42: "Tipaza", 43: "Mila",
                    44: "Aïn Defla", 45: "Naâma", 46: "Aïn Témouchent", 47: "Ghardaïa",
                    48: "Relizane"}


wilaya_number, wilaya_name = 14, algerian_wilayas[14]
place_name = f"{wilaya_name}, Algeria"
graph = ox.graph_from_place(place_name, network_type='drive')
ox.plot_graph(ox.project_graph(graph))



ox.save_graphml(graph, f"./Graphs/GraphML/{wilaya_number}_{wilaya_name}.graphml")
ox.save_graph_xml(graph, f"./Graphs/OSM/{wilaya_number}_{wilaya_name}.osm")
