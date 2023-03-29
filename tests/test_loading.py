import json
from langflow.graph.graph import Graph
import pytest

from langflow import load_flow_from_json
from langflow.utils.payload import get_root_node
from langchain.agents import AgentExecutor


def test_load_flow_from_json():
    """Test loading a flow from a json file"""
    loaded = load_flow_from_json(pytest.BASIC_EXAMPLE_PATH)
    assert loaded is not None
    assert isinstance(loaded, AgentExecutor)


def test_get_root_node():
    with open(pytest.BASIC_EXAMPLE_PATH, "r") as f:
        flow_graph = json.load(f)
    data_graph = flow_graph["data"]
    nodes = data_graph["nodes"]
    edges = data_graph["edges"]
    graph = Graph(nodes, edges)
    root = get_root_node(graph)
    assert root is not None
    assert hasattr(root, "id")
    assert hasattr(root, "data")
