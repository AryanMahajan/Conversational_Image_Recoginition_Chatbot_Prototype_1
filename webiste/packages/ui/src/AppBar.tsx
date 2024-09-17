


export const AppBar = () => {
    return <nav className="h-20 border-gray-200 border flex items-center">
        <div className="relative w-[1080px] mx-auto flex items-center justify-between ">
            <a href="/">
                <img src="https://www.chatbot.com/chatbot-logo.svg" height={133} width={133} alt="Chat Bot Logo"></img>
            </a>
            <ul className="flex space-x-7">
                <li className="text-black font-semibold font-mulish hover:text-gray-500 cursor-pointer transition-all duration-200 relative group">Product</li>
                <li className="text-black font-semibold font-mulish hover:text-gray-500 cursor-pointer transition-all duration-200 relative group">Pricing</li>
                <li className="text-black font-semibold font-mulish hover:text-gray-500 cursor-pointer transition-all duration-200 relative group">Integration</li>
                <li className="text-black font-semibold font-mulish hover:text-gray-500 cursor-pointer transition-all duration-200 relative group">Resources</li>
            </ul>
            <div className="flex">
            
                <div >
                    <button type="button" className="text-black transition-all duration-200 bg-white border-black border-2 hover:bg-black hover:text-white font-semibold rounded-lg text-sm px-5 py-2.5 me-2 mb-2 focus:outline-none">Log in</button>
                </div>
                <div>
                    <button type="button" className="text-white transition-all duration-200 bg-blue-700 hover:bg-blue-800 font-semibold rounded-lg text-sm px-5 py-3 me-2 mb-2 focus:outline-none">Sign up</button>
                </div>
            </div>
        </div>
    </nav>
}