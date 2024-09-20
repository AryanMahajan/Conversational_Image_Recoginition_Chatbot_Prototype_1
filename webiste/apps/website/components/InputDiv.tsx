"use client";
import React, { useEffect, useRef, useState } from "react";

const InputDiv = () => {
    const [value, setValue] = useState("");
    const textareaRef = useRef<HTMLTextAreaElement>(null);

    const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        setValue(e.target.value);
    };

    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
            textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
            // Set a maximum height for the textarea to enable scrolling
            if (textareaRef.current.scrollHeight > 350) { // 150px max height for example
                textareaRef.current.style.height = '350px';
                textareaRef.current.style.overflowY = 'auto'; // Enable vertical scrolling
            } else {
                textareaRef.current.style.overflowY = 'hidden';
            }
        }
    }, [value]);

    return (
        <div className="relative w-full max-w-2xl mb-4">
            <textarea
                ref={textareaRef}
                onChange={handleInputChange}
                value={value}
                placeholder="Message ChatBot"
                rows={1} // Minimum rows visible
                className="rounded-xl pl-4 pr-20 bg-zinc-600 py-3 border-none focus:outline-none text-slate-50 w-full resize-none "
                
            />
            <div className={`absolute right-2 bottom-1 transform -translate-y-7 mr-3 bg-white rounded-full p-1 ${!value.trim() ? "opacity-50 cursor-not-allowed pointer-events-none" : "cursor-pointer"} `}>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="size-6">
                    <path fillRule="evenodd" d="M11.47 2.47a.75.75 0 0 1 1.06 0l7.5 7.5a.75.75 0 1 1-1.06 1.06l-6.22-6.22V21a.75.75 0 0 1-1.5 0V4.81l-6.22 6.22a.75.75 0 1 1-1.06-1.06l7.5-7.5Z" clipRule="evenodd" />
                </svg>
            </div>
            <div className="text-gray-400 flex justify-center text-xs group">
                ChatBot can make mistakes. Check important info.
            </div>
        </div>
    );
}

export default function UserInput() {
    return (
        <div className="fixed bottom-0 w-full p-4 flex justify-center">
            <InputDiv />
        </div>
    );
}
