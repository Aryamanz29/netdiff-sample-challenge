import json
from copy import deepcopy
from netdiff.parsers.base import BaseParser


class ZeroTierParser(BaseParser):
    protocol = 'ZeroTier Peers Information'
    version = '1'
    metric = 'static'

    def to_python(self, data):
        if isinstance(data, list):
              return data
        return super().to_python(data)

    def parse(self, data):
        graph = self._init_graph()
        for peer in data:
            peer_properties = deepcopy(peer)
            peer_properties.pop('paths', {})
            peer_address = peer.get('address')
            graph.add_node(peer_address, **peer_properties)
            self._parse_peer_paths_edge(graph, peer)
        return graph

    def _parse_peer_paths_edge(self, graph, peer):
        peer_paths = peer.get('paths')
        peer_address = peer.get('address')
        peer_path_cost = peer.get('latency')
        for path in peer_paths:
            path_address = path.get('address')
            graph.add_edge(
                peer_address, path_address, weight=peer_path_cost, **path
            )
