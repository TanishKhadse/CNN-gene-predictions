import {motion} from "framer-motion"
import Backdrop from "./backdrop";
import { BiX } from "react-icons/bi";

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
                    bg-neutral-300
                    shadow-lg
                    relative
                "
                variants={dropIn}
                intial="hidden"
                animate="visible"
                exit="exit"
            >
                <div class="cursor-pointer absolute left-0 hover:text-red-500 p-2">
                    <BiX onClick={() => onClose()}/>
                </div>
                <div class="text-black text-lg font-normal py-3">   
                    Set number of outputted genes:
                </div>
                <input
                    type="text"
                    id="num"
                    placeholder="10"
                    class=""
                >
                </input>
            </motion.div>
        </Backdrop>
    )
}