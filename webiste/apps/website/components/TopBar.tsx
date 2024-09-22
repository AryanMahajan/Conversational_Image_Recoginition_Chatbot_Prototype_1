"use client"
import { usePathname, useRouter } from "next/navigation";


export const TopBar = () : JSX.Element => {
    const router = useRouter();
    const pathname = usePathname();
    console.log(pathname)
    return <div>
        <div className=" text-white px-10 pt-4">
            <div className='flex justify-between font-mono text-lg font-semibold'>
                <a href="/dashboard">
                    <p className="">ChatBot</p>
                </a>
                <ol className='flex '>
                    <div className='flex space-x-16 font-mono text-lg font-semibold flex-row justify-center'>
                        <li className={`cursor-pointer ${pathname === "/chat"? "text-blue-400" : "hover:text-blue-400"}  transition-all duration-200`} onClick={() => { router.push("/chat")}}>AI Chat</li>
                        <li className={`cursor-pointer ${pathname === "/imageChecker"? "text-blue-400" : "hover:text-blue-400"}  transition-all duration-200`} onClick={() => { router.push("/imageChecker")}}>AI Image Checker</li>
                        <li className={`cursor-pointer ${pathname === "/contact"? "text-blue-400" : "hover:text-blue-400"}  transition-all duration-200`} onClick={() => { router.push("/contact")}}>Contact</li>
                        <li className={`cursor-pointer ${pathname === "/profile"? "text-blue-400" : "hover:text-blue-400"}  transition-all duration-200`} onClick={() => { router.push("/profile")}}>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                            </svg>
                        </li>
                    </div>
                </ol>
            </div>
        </div>
    </div>
};