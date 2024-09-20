
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
                <input placeholder="Enter your email " className="border-2 shadow-sm hover:bg-slate-50 transition-all duration-200 focus:bg-slate-100 border-black py-4 pl-6 text-xl pr-24 rounded-2xl" type="text"/>
                <div className="flex justify-center ml-2 pt-1 ">
                    <button type="button" className="text-white transition-all duration-200 bg-blue-700 hover:bg-blue-800 font-semibold rounded-lg text-lg px-10 py-4 me-2 mb-2 focus:outline-none">START FREE TRIAL</button>
                </div>
            </div>
            <div className="flex">
                <div className="bg-slate-100 shadow-xl hover:bg-slate-200 transition-all duration-200 px-8 pb-8 py-10 w-custom rounded-xl relative mt-10 flex-col items-center">
                    <div className="absolute top-0 left-1/2 transform -translate-x-1/2 mt-10">
                        <img src="https://github.com/AryanMahajan/Conversational_Image_Recoginition_Chatbot/raw/main/webiste/packages/ui/src/assets/1.png" className="rounded-full w-24 h-24 object-cover"  alt="Bot " />
                    </div>
                    <div className="mt-60 text-5xl font-extrabold text-center">
                        Standalone AI
                    </div>
                    <div className="text-center mt-10 px-4">No dependencies on third-party providers like OpenAI, Google Bard or Bing AI.</div>
                </div>
                <div className="bg-slate-100 shadow-xl hover:bg-slate-200 transition-all duration-200 ml-10 px-8 pb-8 py-10 w-custom rounded-xl relative mt-10 flex-col items-center">
                    <div className="absolute top-0 left-1/2 transform -translate-x-1/2 mt-10">
                        <img src="https://github.com/AryanMahajan/Conversational_Image_Recoginition_Chatbot/raw/main/webiste/packages/ui/src/assets/1.png" className="rounded-full w-24 h-24 object-cover"  alt="Bot " />
                    </div>
                    <div className="mt-60 text-5xl font-extrabold text-center">
                        Data secured
                    </div>
                    <div className="text-center mt-10 px-4">All data is processed and hosted only in the ChatBot platform.</div>
                </div>
            </div>
            

        </div>
    );
};
