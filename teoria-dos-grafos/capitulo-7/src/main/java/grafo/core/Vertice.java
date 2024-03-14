package main.java.grafo.core;

public class Vertice {
	private String rotulo;
	private int grau;

	public Vertice(String rotulo) throws Exception {
		boolean isRotuloNullOrBlank = rotulo == null || rotulo != null && "".equals(rotulo.trim());
		if (isRotuloNullOrBlank) {
			throw new Exception("N�o � permitida a inclus�o de v�rtices com r�tulo em branco.");
		}
		this.rotulo = rotulo;
	}

	public String getRotulo() {
		return this.rotulo;
	}
	
	void addGrau(){
	    grau++;
	}

	public int getGrau() {
		return grau;
	}
}
