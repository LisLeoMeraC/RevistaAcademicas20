package com.example.revistaacademicas;

import android.content.Context;
import android.support.annotation.NonNull;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

import java.util.List;

public class Adaptador extends RecyclerView.Adapter<Adaptador.ViewHolder> {
    LayoutInflater inflater;
    List<Revista> revistas;

    public Adaptador(Context ctx, List<Revista> revistas){
        this.inflater = LayoutInflater.from(ctx);
        this.revistas = revistas;
    }





    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = inflater.inflate(R.layout.lista_revista,parent,false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        // bind the data
        holder.issue.setText(revistas.get(position).getIssue_id());
        holder.vol.setText(revistas.get(position).getVolume());
        holder.num.setText(revistas.get(position).getNumber());
        holder.year.setText(revistas.get(position).getYear());
        holder.date.setText(revistas.get(position).getDate_published());
        holder.title.setText(revistas.get(position).getTitle());
        holder.doi.setText(revistas.get(position).getDoi());
        Picasso.get().load(revistas.get(position).getCover()).into(holder.CoverImage);

    }

    @Override
    public int getItemCount() {
        return revistas.size();
    }

    public  class ViewHolder extends  RecyclerView.ViewHolder{
        TextView issue,vol,num,year,date,title,doi;
        ImageView CoverImage;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);

            issue = itemView.findViewById(R.id.issue_id);
            vol = itemView.findViewById(R.id.volume);
            CoverImage = itemView.findViewById(R.id.coverImage);
            num = itemView.findViewById(R.id.number);
            year = itemView.findViewById(R.id.year);
            date = itemView.findViewById(R.id.date_published);
            title = itemView.findViewById(R.id.title);
            doi = itemView.findViewById(R.id.doi);

            // handle onClick

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Toast.makeText(v.getContext(), "Do Something With this Click", Toast.LENGTH_SHORT).show();
                }
            });
        }
    }
}
