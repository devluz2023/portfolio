package main.java.grafo.core;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class Grafo {
	private int qtdMaximaVertices;
	private boolean isQtdMaximaDefinida;
	private int qtdAtualVertices = 0;
	private Map<String, Integer> rotulosEmIndices = new HashMap<String, Integer>();
	private List<Vertice> vertices = new ArrayList<Vertice>();
	private MatrizAdjacencia matrizAdjacencia;

	public Grafo() {
		qtdMaximaVertices = 10;
	}

	public Grafo(int qtdVertices) {
		if (qtdVertices <= 0) {
			throw new IllegalArgumentException("A quantidade m�xima de v�rtices deve ser maior ou igual � 1");
		}
		qtdMaximaVertices = qtdVertices;
		isQtdMaximaDefinida = true;
	}

	public void adicionarVertice(String rotulo) throws Exception {
		if (qtdAtualVertices <= qtdMaximaVertices - 1) {
			Vertice novoVertice = new Vertice(rotulo);
			this.vertices.add(novoVertice);
			this.rotulosEmIndices.put(rotulo, qtdAtualVertices);
			qtdAtualVertices++;
		} else {
			throw new Exception("A quantidade de v�rtices permitida (" + qtdMaximaVertices + ")	foi	excedida.");
		}
	}
	
	public List<Vertice> getVertices(){
		return this.vertices;
	}
	
	public Vertice getVertice(String rotulo) {
		this.existeVerticeOrThrow(rotulo);
		int indice = this.rotulosEmIndices.get(rotulo);
		return this.vertices.get(indice);
	}
	
	public void conectarVertices(String rotuloVerticeInicial, String rotuloVerticeFinal) throws Exception{
		if(!this.existeVertice(rotuloVerticeInicial) || !this.existeVertice(rotuloVerticeFinal)) {
    		throw new Exception("Para adicionar uma aresta ambos os v�rtices devem existir.");
    	}
	    criarMatrizAdjacencia();
	    int indiceVerticeFinal = this.rotulosEmIndices.get(rotuloVerticeInicial);
		int indiceVerticeInicial = this.rotulosEmIndices.get(rotuloVerticeFinal);
		this.matrizAdjacencia.adicionarAresta(indiceVerticeInicial, indiceVerticeFinal);
	}
	
	public List<Vertice> getAdjacencias(String vertice) {
		this.existeVerticeOrThrow(vertice);
		int indiceVertice = this.rotulosEmIndices.get(vertice);
		return this.matrizAdjacencia.getAdjacencias(indiceVertice);
	}
	
	private boolean existeVerticeOrThrow(String vertice) {
		if(!existeVertice(vertice)) {
			throw new IllegalArgumentException("O v�rtice n�o existe.");
		}
		return true;
	}
	
	private boolean existeVertice(String rotuloVertice) {
		return this.rotulosEmIndices.get(rotuloVertice) != null ? true : false;
	}

	private void criarMatrizAdjacencia() {
	    if(this.matrizAdjacencia == null){
	        this.matrizAdjacencia = new MatrizAdjacencia(new ArrayList<Vertice>(this.vertices));
	    }
	}
	
	public Grafo arvoreGeradoraPorProfundidade() throws Exception {
		Grafo arvore = new Grafo();
		Stack<Vertice> roloDeBarbante = new Stack<Vertice>();
		LinkedHashSet<String> verticesVisitados = new LinkedHashSet<String>();
		List<Vertice> vertices = getVertices();

		for(Vertice v : vertices) {
			arvore.adicionarVertice(v.getRotulo());
		}
		
		Vertice verticePontoDePartida = vertices.get(0);
        verticesVisitados.add(verticePontoDePartida.getRotulo());
        roloDeBarbante.push(verticePontoDePartida);

        while(!roloDeBarbante.empty()){
        	Vertice verticeAnalisado = roloDeBarbante.peek();
            Vertice proximoVertice = obterProximoVertice(verticeAnalisado, verticesVisitados);
            if(proximoVertice == null){
                roloDeBarbante.pop();
            } else {
            	String rotulo = proximoVertice.getRotulo();
            	verticesVisitados.add(rotulo);
                roloDeBarbante.push(proximoVertice);
                arvore.conectarVertices(verticeAnalisado.getRotulo(), proximoVertice.getRotulo());
            }
        }

		return arvore;
	}
	
	private Vertice obterProximoVertice(Vertice vertice, LinkedHashSet<String> verticesVisitados){
    	List<Vertice> adjacencias = getAdjacencias(vertice.getRotulo());
        for(int i=0; i<adjacencias.size(); i++){
        	Vertice adjacencia = adjacencias.get(i);
        	boolean naoVisitadoAinda = !verticesVisitados.contains(adjacencia.getRotulo());
            if(naoVisitadoAinda){
                return adjacencia;
            }
        }
        return null;
    }
}
