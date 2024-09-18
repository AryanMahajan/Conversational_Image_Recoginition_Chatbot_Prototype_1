
export const TopBar = () : JSX.Element => {
    return <div>
        <div className=" text-white px-10 pt-3">
            <div className='flex justify-between font-mono text-lg font-semibold'>
                <a href="/">
                    <p>ChatBot</p>
                </a>
                <ol className='flex '>
                    <div className='flex space-x-16 font-mono text-lg font-semibold flex-row justify-center'>
                        <li className='cursor-pointer hover:text-blue-400 transition-all duration-200'>AI Chat</li>
                        <li className='cursor-pointer hover:text-blue-400 transition-all duration-200'>AI Image Checker</li>
                        <li className='cursor-pointer hover:text-blue-400 transition-all duration-200'>Services</li>
                        <li className='cursor-pointer hover:text-blue-400 transition-all duration-200'>Contact</li>
                        <li className='cursor-pointer hover:text-blue-400 transition-all duration-200'>
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