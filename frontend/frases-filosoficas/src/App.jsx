import { useState } from 'react';

export default function App() {
  const [frase, setFrase] = useState('');

  function requisicao() {
  fetch('http://127.0.0.1:5000')
    .then(response => response.json())
    .then(data => {
      return setFrase(`${data.chave}: ${data.valor}`);
    })
    .catch(error => {
      setFrase('Erro ao buscar frase');
    });
}

  return (
    <>
    <div class="container">
    <div>
      <h1>Gerador de frases filosóficas</h1>
      <h2>Clique no botão para gerar uma frase aleatória</h2>
      <button onClick={requisicao}>Gerar frase</button>
      <p>{frase}</p>
      </div>
      </div>
    </>
  );
}