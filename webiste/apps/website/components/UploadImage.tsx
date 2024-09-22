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
                
            /> : <div className="mt-2">
                    <ul>
                        {images.map((image, index) => (
                            <li key={index} className="mt-2 text-white">
                                <p><strong>File Key:</strong> {image.fileKey}</p>
                                <p><strong>File Name:</strong> {image.fileName}</p>
                                <Image src={image.fileKey} alt={image.fileName} width={200} height={200} />
                            </li>
                        ))}
                    </ul>
                </div>
            }
        </main>
    );
}
