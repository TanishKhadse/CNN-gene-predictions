import { useState } from "react"
import Entry from "./entry"

export default function GeneList({}) {

    const [genes, setGenes] = useState([
        "pull", 
        "data", 
        "from", 
        "api", 
        "number of genes from options", 
        "p-scores too"
    ])

    return (
        <div class="w-[25vw]">
            <div class="pl-4 pt-4 flex flex-col pr-4 pb-4">
                <div class="text-xl pb-4">
                    Genes
                </div>
                <div class="border-[1px] border-neutral-500 rounded-sm h-96">
                    {
                    genes.map((g) => 
                        ( <Entry name={g} /> )
                        )
                    }
                </div>

            </div>
        </div>
    )
}