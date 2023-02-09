import osmnx as ox

# dict of algerian wilayas and their codes

algerian_wilayas = {
    "Adrar": "01","Chlef": "02","Laghouat": "03","Oum El Bouaghi": "04",
    "Batna": "05","Béjaïa": "06","Biskra": "07","Béchar": "08",
    "Blida": "09","Bouira": "10","Tamanrasset": "11","Tébessa": "12",
    "Tlemcen": "13","Tiaret": "14","Tizi Ouzou": "15","Alger": "16",
    "Djelfa": "17","Jijel": "18","Sétif": "19","Saïda": "20",
    "Skikda": "21","Sidi Bel Abbès": "22","Annaba": "23","Guelma": "24",
    "Constantine": "25","Médéa": "26","Mostaganem": "27","M'Sila": "28",
    "Mascara": "29","Ouargla": "30","Oran": "31","El Bayadh": "32",
    "Illizi": "33","Bordj Bou Arreridj": "34","Boumerdès": "35",
    "El Tarf": "36","Tindouf": "37","Tissemsilt": "38","El Oued": "39",
    "Khenchela": "40","Souk Ahras": "41","Tipaza": "42","Mila": "43",
    "Aïn Defla": "44","Naâma": "45","Aïn Témouchent": "46","Ghardaïa": "47",
    "Relizane": "48"
}

inverse_algerian_wilayas = {int(v): k for k, v in algerian_wilayas.items()}


wilaya_number,wilaya_name = 27 , inverse_algerian_wilayas[27]
place_name = f"{wilaya_name}, Algeria"
graph = ox.graph_from_place(place_name, network_type='drive')
ox.plot_graph(ox.project_graph(graph))


# nx.write_gexf(graph, f"./Graphs/GEXF/{wilaya_number}_{wilaya_name}.gexf")
# nx.write_graphml(graph, f"./Graphs/GraphML/{wilaya_number}_{wilaya_name}.graphml")
# nx.write_gml(graph, f"./Graphs/GML/{wilaya_number}_{wilaya_name}.gml")
ox.save_graphml(graph, f"./Graphs/GraphML/{wilaya_number}_{wilaya_name}.graphml")
ox.save_graph_xml(graph, f"./Graphs/OSM/{wilaya_number}_{wilaya_name}.osm")