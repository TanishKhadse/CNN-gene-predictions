export default function Node({gene}) {
    return (
        <div>
            <div class="
                rounded-full 
                border-[1px] 
                w-[50px] 
                h-[50px] 
                border-neutral-500 
                flex 
                items-center 
                justify-center
                select-none
                cursor-pointer
            ">
                <p>{gene.name}</p>
            </div>
        </div>
    )
}