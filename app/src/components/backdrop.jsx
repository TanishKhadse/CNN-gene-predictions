import { motion } from "framer-motion"

export default function Backdrop({children, onClick}) {

    return (
        <motion.div
            class="
                absolute 
                top-0 
                left-0
                w-[100%] 
                h-[100%]
                bg-black
                opacity-60
                flex
                items-center
                justify-center
            "
            initial={{opacity: 0}}
            animate={{opacity: 0.75}}
            exit = {{opacity: 0}}
            onClick={onClick}
        >
            {children}
        </motion.div>
    )
}