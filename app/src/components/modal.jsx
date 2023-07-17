import { useState, useCallback, useEffect } from "react";
import {motion} from "framer-motion"
import Backdrop from "./backdrop";

export default function Modal({isOpen, onClose}) {

    const dropIn = {
        hidden: {y: "-100vh",  opacity: 0}, 
        visible:{y: "0"},
        exit: {y: "-100vh", opacity: 0},
    }

    return (
        <Backdrop onClick={onClose}>
            <motion.div
                onClick={(e) => e.stopPropagation()}
                class="
                    rounded-lg
                    flex
                    flex-col
                    items-center
                    m-auto
                    w-[30%]
                    h-[50%]
                    bg-neutral-700
                "
                variants={dropIn}
                intial="hidden"
                animate="visible"
                exit="exit"
            >
                <div class="text-white">   
                    Set number of outputted genes:
                </div>

            </motion.div>
        </Backdrop>
    )
}