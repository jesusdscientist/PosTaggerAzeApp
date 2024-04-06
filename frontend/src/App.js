import logo from './logo.svg';
import backgroundImage from './background.jpg';
import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [sentence, setSentence] = useState('');
  const [tags, setTags] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/tag', { text: sentence });
      setTags(response.data.tags);
    } catch (error) {
      console.error('There was an error tagging the sentence:', error);
      // Handle the error state appropriately
    }
  };


  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      <h1 className="text-6xl font-bold mb-8 text-white">Aze Pos Tagger App</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          value={sentence}
          onChange={(e) => setSentence(e.target.value)}
          className="shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline mr-4"
          placeholder="Enter a sentence"
        />
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Tag Sentence
        </button>
      </form>
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <h2 className="text-xl mb-8 w-80 font-bold text-center">Tags</h2>
        <div className="flex flex-wrap">
          {tags.map((tag, index) => (
            <span
              key={index}
              className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>

  </div>







  );
}

export default App;
