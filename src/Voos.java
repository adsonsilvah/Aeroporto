public class Voos {

    private String aerOrigem;
    private String aerDestino;
    private long id;
    //colocar data e hora
    private String classe;
    private String tipoClasse;
    private int QtdAssentos;

    public Voos(String aerOrigem, String aerDestino,long id, String classe,
                String tipoClasse, int QtdAssentos) {
        this.aerOrigem = aerOrigem;
        this.aerDestino = aerDestino;
        this.id = id;
        this.classe = classe;
        this.tipoClasse = tipoClasse;
        this.QtdAssentos = QtdAssentos;
    }
    public String getAerOrigem() {
        return aerOrigem;
    }
    public void setAerOrigem(String aerOrigem) {
        this.aerOrigem = aerOrigem;
    }
    public String getAerDestino() {
        return aerDestino;
    }
    public void setAerDestino(String aerDestino) {
        this.aerDestino = aerDestino;
    }
    public String getClasse() {
        return classe;
    }
    public void setClasse(String classe) {
        this.classe = classe;
    }
    public String getTipoClasse() {
        return tipoClasse;
    }
    public void setTipoClasse(String tipoClasse) {
        this.tipoClasse = tipoClasse;
    }
    public long getId() {
        return id;
    }
    public void setId(long id) {
        this.id = id;
    }

    public int getQtdAssentos() {
        return QtdAssentos;
    }

    public void setQtdAssentos(int qtdAssentos) {
        QtdAssentos = qtdAssentos;
    }
    public void verificaVoo(){
        if(aerDestino.equals(aerOrigem)){
            System.out.println("Voo não podem ter mesma origem e destino");
        }
    }

}