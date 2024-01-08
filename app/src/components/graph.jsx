import Node from "./node";
import React, { useEffect } from 'react'
import Graph from 'react-vis-network-graph'
import { useState } from "react";

export default function GraphView({graph_data}) {

    const [graph, setGraph] = useState({})
    let nodes = [];
    let edges = [];

    /**
     * form:
     * graph_data[0] --> disease
     * graph_data[1:] --> genes
     */

    useEffect(() => {

        graph_data.forEach((node,id) => {
            nodes.push({id: id, label: node.name, shape: "circle", color: "skyblue"})
            if (id > 0) {
                edges.push({from: id, to: 0})
            }
        })
    
        setGraph({nodes: nodes, edges: edges})

    }, [graph_data])

    
    // {
    //     nodes: [
    //         {id: 1, label: "Node 1", shape: "circle", color: "skyblue"},
    //         {id: 2, label: "Node 2", shape: "circle", color: "pink"},
    //         {id: 3, label: "Node 3", shape: "circle", color: "pink"},
    //         {id: 4, label: "Node 4", shape: "circle", color: "pink"},
    //     ],
    //     edges: [
    //         {from: 2, to: 1},
    //         {from: 3, to: 1},
    //         {from: 4, to: 1},
    //     ]
    // }

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