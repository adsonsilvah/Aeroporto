public class Passagem{
    private long id;
    private String nomePassag;
    private long cpf;
    private double valorPassagem;

    public Passagem(long id, String nomePassag, long cpf, double valorPassagem){
        this.id = id;
        this.nomePassag = nomePassag;
        this.valorPassagem = valorPassagem;
        this.cpf = cpf;
    }
    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }
    public String getNomePassag() {
        return nomePassag;
    }

    public void setNomePassag(String nomePassag) {
        this.nomePassag = nomePassag;
    }
    public long getCpf() {
        return cpf;
    }

    public void setCpf(long cpf) {
        this.cpf = cpf;
    }

    public double getValorPassagem() {
        return valorPassagem;
    }

    public void setValorPassagem(double valorPassagem) {
        this.valorPassagem = valorPassagem;
    }
}
