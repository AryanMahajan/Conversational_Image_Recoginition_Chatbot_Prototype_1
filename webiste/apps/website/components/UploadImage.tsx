"use client";

import "@uploadthing/react/styles.css";
import Image from 'next/image';
import { generateUploadDropzone } from "@uploadthing/react";
import type { OurFileRouter } from "../app/api/uploadthing/core";
import { useState, useEffect } from "react";

const UploadDropzone = generateUploadDropzone<OurFileRouter>();


export const UploadImage = () => {
    const [images, setImages] = useState<{ fileKey: string; fileName: string }[]>([]);

    useEffect(() => {
        if (images.length > 0) {
            console.log("Updated Images State:", images);
        }
    }, [images]);
    const handleUploadError = (error: Error) => {
        console.error("Upload Error:", error);
        alert(`ERROR! ${error.message}`);
    };

    return (
        <main className="flex flex-col items-center justify-center">
            {images.length == 0 ? <UploadDropzone className="bg-slate-300 font-bold"
                endpoint="imageUploader"
                onClientUploadComplete={(res) => {
                    if (res && res.length > 0) {
                        const uploadedImages = res.map(file => ({
                            fileKey: file.appUrl || "",
                            fileName: file.name || ""
                        }));
                        setImages(uploadedImages);
                    }
                    console.log("Upload Complete:", res);
                    alert("Upload Completed");
                }}
                onUploadError={handleUploadError}
                
            /> : <div className="mt-2 w-[720px]">
                    <ul>
                        {images.map((image, index) => (
                            <li key={index} className="mt-2 text-white">
                                <p><strong>File Key: </strong>{image.fileKey}</p>
                                <ImageLoader src={image.fileKey} alt={image.fileName} />
                            </li>
                        ))}
                    </ul>
                </div>
            }
        </main>
    );
}


const ImageLoader = ({ src, alt }: {src: string, alt: string}) => {
    const [loading, setLoading] = useState(true);

    const handleLoad = () => {
        setTimeout(() => {
            setLoading(false);
        },5000)
    };
    return (
        <div className="relative">
            {loading && (
                <div
                    className="absolute inline-block h-8 mt-32 ml-32 w-8 animate-spin rounded-full border-4 border-solid border-current border-r-transparent align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
                    role="status">
                    <span className="!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">Loading...</span>
                </div>
            )}
            <Image className="absolute inset-0 flex items-center mt-4 justify-center rounded-lg border-2 border-white w-[300]"
                src={src}
                alt={alt}
                width={300}
                height={300}
                onLoad={handleLoad}
            />
        </div>
    );
};