import Node from "./node";
import React from 'react'
import Graph from 'react-vis-network-graph'

export default function GraphView({}) {

    const graph = {

        nodes: [
            {id: 1, label: "Node 1", shape: "circle", color: "skyblue"},
            {id: 2, label: "Node 2", shape: "circle", color: "pink"},
            {id: 3, label: "Node 3", shape: "circle", color: "pink"},
            {id: 4, label: "Node 4", shape: "circle", color: "pink"},
            {id: 5, label: "Node 5", shape: "circle", color: "pink"},
            {id: 6, label: "Node 6", shape: "circle", color: "pink"},
            {id: 7, label: "Node 7", shape: "circle", color: "pink"},
            {id: 8, label: "Node 8", shape: "circle", color: "pink"},
            {id: 9, label: "Node 9", shape: "circle", color: "pink"},
        ],
        edges: [
            {from: 2, to: 1},
            {from: 3, to: 1},
            {from: 4, to: 1},
            {from: 5, to: 1},
            {from: 6, to: 1},
            {from: 7, to: 1},
            {from: 8, to: 1},
            {from: 9, to: 1},
            
        ]

    }
    const option = {
        edges: {
            color: "gray"
        },
        height: "500px"
    }
    return (
        <div class="w-[75vw] h-48">
            <Graph 
                graph={graph}
                options={option}
            />
            
        </div>
    )
}