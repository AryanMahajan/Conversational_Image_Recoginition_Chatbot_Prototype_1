import botLogo from "./assets/1.png"

export const HeroSec = () => {
    return (
        <div className="flex items-center flex-col mt-20">
            <div className="relative mx-auto flex items-center justify-between text-7xl font-extrabold font-serif">
                Help customers instantly
            </div>
            <div className="relative mx-auto flex items-center justify-between text-7xl font-extrabold font-serif">
                with an&nbsp;<span className="text-blue-500">AI-driven</span>&nbsp;chatbot
            </div>
            <div className="relative flex items-center justify-between max-w-2xl font-mulish font-medium text-2xl mt-4">
                ChatBot scans your provided images to provide quick and accurate AI-generated answers to customer questions.
            </div>
            <div className="mt-20 flex">
                <input placeholder="Enter your email " className="border-2 focus:bg-slate-100 border-black py-4 pl-6 text-xl pr-24 rounded-2xl" type="text"/>
                <div className="flex justify-center ml-2 pt-1">
                    <button type="button" className="text-white transition-all duration-200 bg-blue-700 hover:bg-blue-800 font-semibold rounded-lg text-lg px-10 py-4 me-2 mb-2 focus:outline-none">Sign up Free</button>
                </div>
            </div>
            <div>
                <img src={botLogo} alt="Bot " />
            </div>
        </div>
    );
};
