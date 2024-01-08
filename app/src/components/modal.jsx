import {motion} from "framer-motion"
import Backdrop from "./backdrop";
import { BiX } from "react-icons/bi";
import { useState, useRef, useCallback } from "react";

export default function Modal({isOpen, onClose, handleModalData}) {
    const diseaseInputRef = useRef(null)
    const nodesInputRef = useRef(null)


    const dropIn = {

        hidden: {y: "-100vh",  opacity: 1}, 
        visible:{y: "0"},
        exit: {y: "-100vh", opacity: 1},
    }

    const handleSubmit = async () => {
        const disease_name = diseaseInputRef.current.value
        let num_nodes = nodesInputRef.current.value
        if (!num_nodes) {
            num_nodes = 10
        }

        // extract values from disease_name and num_nodes

        fetch("/graph", {
            method: "POST", 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({disease_name: disease_name, num_nodes: num_nodes})}
        ).then(
            res => res.json()
        ).then(
            data => handleModalData(data)
        ).catch(error => console.log(error))
        

        onClose()
    }

    return (
        <Backdrop onClick={onClose}>
            <motion.div
                onClick={(e) => e.stopPropagation()}
                class="
                    rounded-lg
                    shadow-lg
                    flex
                    flex-col
                    items-center
                    justify-between
                    m-auto
                    w-[30%]
                    h-[35%]
                    bg-slate-300/100
                    relative
                    py-2
                    z-50
                "
                variants={dropIn}
                intial="hidden"
                animate="visible"
                exit="exit"
            >
                <div class="cursor-pointer absolute left-0 top-0 hover:text-red-500 p-2">
                    <BiX onClick={() => onClose()}/>
                </div>
                <div class="text-black text-lg font-normal py-3">   
                    Set number of outputted genes:
                </div>
                <input
                    type="text"
                    id="disease"
                    placeholder="enter a disease"
                    class="outline px-2 py-1 text-center my-2"
                    ref={diseaseInputRef}
                >
                </input>
                <input
                    type="text"
                    id="num"
                    placeholder="(default 10)"
                    class="outline px-2 py-1 text-center my-2 mb-4"
                    ref={nodesInputRef}
                    >
                </input>
                <div class="
                    cursor-pointer 
                    bg-blue-500 
                    hover:bg-blue-400 
                    text-neutral-50 
                    p-2 
                    rounded-xl
                "
                    onClick={handleSubmit}
                >
                    Generate
                </div>
            </motion.div>
        </Backdrop>
    )
}