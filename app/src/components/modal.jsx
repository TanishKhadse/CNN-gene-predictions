import {motion} from "framer-motion"
import Backdrop from "./backdrop";
import { BiX } from "react-icons/bi";
import { useCallback } from "react";

export default function Modal({isOpen, onClose}) {

    const dropIn = {
        hidden: {y: "-100vh",  opacity: 1}, 
        visible:{y: "0"},
        exit: {y: "-100vh", opacity: 1},
    }

    const handleSubmit = useCallback(() => {
        onClose()
    }, [])

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
                    bg-neutral-300
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
                >
                </input>
                <input
                    type="text"
                    id="num"
                    placeholder="(default 10)"
                    class="outline px-2 py-1 text-center my-2 mb-4"
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