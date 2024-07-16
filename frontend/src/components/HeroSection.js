import React from 'react';
import heroHouse from '../assets/images/heroHouse.jpg';
import logo from '../assets/images/logo.png';

function HeroSection() {
    return (
        <div
            className="w-full h-screen bg-cover bg-center grid grid-rows-[10%_80%] gap-2 p-8"
            style={{
                backgroundImage: `linear-gradient(rgba(0,200,10,.5), rgba(0,200,100,.5)), url(${heroHouse})`,
                backgroundBlendMode: 'overlay',
                backgroundSize: 'cover',
            }}
        >
            <img src={logo} alt='Zulu Real Estate Logo' className="size-16 rounded-lg mb-5" />
            <div className='flex flex-col justify-evenly'>
                <div className="text-left">
                    <h1 className="text-4xl font-bold text-white">Unlock Your Real Estate Potential with Data-Driven Insights</h1>
                </div>
                <div className="flex flex-col items-start space-y-4 mb-8 md:flex-row md:items-center">
                    <p className="text-2xl text-white md:w-1/2">Where Data Drives Opportunity.</p>
                    <button className="mt-4 px-8 py-2 bg-gray-500 text-white text-lg font-medium rounded-3xl hover:bg-gray-700 md:mt-0">
                       START
                    </button>
                </div>
            </div>
        </div>
    );
}

export default HeroSection;
